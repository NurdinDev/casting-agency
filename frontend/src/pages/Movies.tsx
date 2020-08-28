import React, { useEffect, useState } from "react";
import {
  IonContent,
  IonHeader,
  IonPage,
  IonTitle,
  IonToolbar,
  IonList,
  IonItem,
  IonLabel,
  IonChip,
  IonFab,
  IonFabButton,
  IonIcon,
  IonItemOption,
  IonItemOptions,
  IonItemSliding,
  IonText,
  IonButtons,
  IonButton,
} from "@ionic/react";
import { API_URL } from "../constants";
import { useHistory } from "react-router-dom";
import { add } from "ionicons/icons";
import MoviesModal from "./MoviesModal";
import { useAuth0 } from "@auth0/auth0-react";

const Movies: React.FC = () => {
  const [movies, setMovies] = useState([]);
  const [actors, setActors] = useState([]);
  const [error, setError] = useState(null);
  const [token, setToken] = useState("");
  const [editedMovie, setEditedMovie] = useState({});
  const [isEdit, setIsEdit] = useState(false);
  const [showModal, setShowModal] = useState(false);
  const history = useHistory();
  const {
    logout,
    loginWithRedirect,
    isAuthenticated,
    getAccessTokenSilently,
  } = useAuth0();

  const deleteMovie = async (id: any) => {
    const res = await fetch(`${API_URL}/movies/${id}`, {
      method: "DELETE",
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });

    const json = await res.json();

    if (json["success"]) {
      setMovies(movies.filter((item: any) => item.id !== id));
    }
  };

  const editMovie = (movie: any) => {
    setEditedMovie(movie);
    setIsEdit(true);
    setShowModal(true);
  };

  const onSubmit = async (data: any) => {
    if (!isEdit) {
      const res = await fetch(`${API_URL}/movies`, {
        method: "POST",
        headers: {
          Authorization: `Bearer ${token}`,
          "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
      });

      const json = await res.json();

      if (json["success"]) {
        setShowModal(false);
        setMovies(json.movies);
      }
    } else {
      const { id }: any = editedMovie;
      const res = await fetch(`${API_URL}/movies/${id}`, {
        method: "PATCH",
        headers: {
          Authorization: `Bearer ${token}`,
          "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
      });

      const json = await res.json();

      if (json["success"]) {
        setShowModal(false);
        setMovies(json.movies);
      }
    }
  };

  useEffect(() => {
    (async () => {
      try {
        const token = await getAccessTokenSilently();
        setToken(token);

        fetch(`${API_URL}/movies`, {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        })
          .then((response) => response.json())
          .then((data) => {
            if (data.success) {
              setMovies(data.movies);
            } else {
              setError(data.message.description);
            }
          })
          .catch((err) => console.log(err));

        fetch(`${API_URL}/actors`, {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        })
          .then((response) => response.json())
          .then((data) => {
            if (data.success) {
              setActors(data.actors);
            } else {
              setError(data.message.description);
            }
          })
          .catch((err) => console.log(err));
      } catch (e) {
        console.error({ e });
        if (e.error === "login_required") {
          loginWithRedirect();
        }
      }
    })();
  }, [getAccessTokenSilently, loginWithRedirect]);

  // useEffect(() => {
  //   (async () => {
  //     try {
  //       const token = await getAccessTokenSilently();
  //       console.log(token);
  //       setToken(token);
  //     } catch (e) {
  //       console.error(e);
  //     }
  //   })();
  // }, [getAccessTokenSilently]);

  return (
    <IonPage>
      <IonHeader>
        <IonToolbar>
          <IonTitle>Movies</IonTitle>
          <IonButtons slot="secondary">
            {!isAuthenticated ? (
              <IonButton color="secondary" onClick={() => loginWithRedirect()}>
                Login
              </IonButton>
            ) : (
              <IonButton color="secondary" onClick={() => logout(
                {
                  returnTo: process.env.IONIC_APP_URL || 'http://localhost:8100'
                }
              )}>
                Log-out
              </IonButton>
            )}
          </IonButtons>
        </IonToolbar>
      </IonHeader>
      <IonContent>
        <IonHeader collapse="condense">
          <IonToolbar>
            <IonTitle size="large">Movies</IonTitle>
          </IonToolbar>
        </IonHeader>
        {isAuthenticated && (
          <IonFab
            vertical="top"
            edge
            horizontal="end"
            slot="fixed"
            onClick={() => setShowModal(true)}
          >
            <IonFabButton>
              <IonIcon icon={add} />
            </IonFabButton>
          </IonFab>
        )}

        {error ? (
          <IonText color="danger">{error}</IonText>
        ) : (
          <IonList>
            {movies.map((movie: any) => (
              <IonItemSliding key={movie.id}>
                <IonItemOptions side="end">
                  <IonItemOption
                    color="danger"
                    onClick={() => deleteMovie(movie.id)}
                  >
                    Delete
                  </IonItemOption>
                  <IonItemOption
                    color="primary"
                    onClick={() => editMovie(movie)}
                  >
                    Edit
                  </IonItemOption>
                </IonItemOptions>
                <IonItem>
                  <IonLabel>
                    <h2>{movie.name}</h2>
                    {movie.actors.map((actor: any) => (
                      <IonChip
                        key={actor.id}
                        onClick={(e) => {
                          e.preventDefault();
                          history.push(`/actors/${actor.id}`);
                        }}
                      >
                        <IonLabel>{actor.name}</IonLabel>
                      </IonChip>
                    ))}
                  </IonLabel>
                </IonItem>
              </IonItemSliding>
            ))}
          </IonList>
        )}
        <MoviesModal
          actors={actors}
          onSubmit={onSubmit}
          isOpen={showModal}
          movie={editedMovie}
          isEdit={isEdit}
          onDidDismiss={() => setShowModal(false)}
        ></MoviesModal>
      </IonContent>
    </IonPage>
  );
};

export default Movies;

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
} from "@ionic/react";
import { API_URL } from "../constants";
import { useHistory } from "react-router-dom";
import { add } from "ionicons/icons";
import MoviesModal from "./MoviesModal";

const Movies: React.FC = () => {
  const [movies, setMovies] = useState([]);
  const [actors, setActors] = useState([]);
  const [editedMovie, setEditedMovie] = useState({});
  const [isEdit, setIsEdit] = useState(false);
  const [showModal, setShowModal] = useState(false);
  const history = useHistory();

  const deleteMovie = async (id: any) => {
    const res = await fetch(`${API_URL}/movies/${id}`, {
      method: "DELETE",
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
    fetch(`${API_URL}/movies`)
      .then((response) => response.json())
      .then((data) => setMovies(data.movies));

    fetch(`${API_URL}/actors`)
      .then((response) => response.json())
      .then((data) => setActors(data.actors));
  }, []);

  return (
    <IonPage>
      <IonHeader>
        <IonToolbar>
          <IonTitle>Movies</IonTitle>
        </IonToolbar>
      </IonHeader>
      <IonContent>
        <IonHeader collapse="condense">
          <IonToolbar>
            <IonTitle size="large">Movies</IonTitle>
          </IonToolbar>
        </IonHeader>
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
                <IonItemOption color="primary" onClick={() => editMovie(movie)}>
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

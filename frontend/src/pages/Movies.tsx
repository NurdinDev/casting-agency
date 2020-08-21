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
} from "@ionic/react";
import "./Movies.css";
import { API_URL } from "../constants";
import { useHistory } from "react-router-dom";

const Movies: React.FC = () => {
  const [movies, setMovies] = useState([]);

  const history = useHistory();

  useEffect(() => {
    fetch(`${API_URL}/movies`)
      .then((response) => response.json())
      .then((data) => setMovies(data.movies));
  }, []);
  return (
    <IonPage>
      <IonHeader>
        <IonToolbar>
          <IonTitle>Movies</IonTitle>
        </IonToolbar>
      </IonHeader>
      <IonContent fullscreen>
        <IonHeader collapse="condense">
          <IonToolbar>
            <IonTitle size="large">Movies</IonTitle>
          </IonToolbar>
        </IonHeader>
        <IonList>
          {movies.map((movie: any) => (
            <IonItem key={movie.id}>
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
          ))}
        </IonList>
      </IonContent>
    </IonPage>
  );
};

export default Movies;

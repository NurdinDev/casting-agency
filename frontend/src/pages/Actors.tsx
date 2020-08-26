import React from "react";
import {
  IonContent,
  IonHeader,
  IonPage,
  IonTitle,
  IonToolbar,
  IonButtons,
  IonButton,
} from "@ionic/react";
import ExploreContainer from "../components/ExploreContainer";
import { useAuth0 } from "@auth0/auth0-react";

const Actors: React.FC = () => {
  const { logout, loginWithRedirect, isAuthenticated } = useAuth0();
  return (
    <IonPage>
      <IonHeader>
        <IonToolbar>
          <IonTitle>Actors</IonTitle>
        </IonToolbar>
        <IonButtons slot="secondary">
          {!isAuthenticated ? (
            <IonButton color="secondary" onClick={() => loginWithRedirect()}>
              Login
            </IonButton>
          ) : (
            <IonButton color="secondary" onClick={() => logout()}>
              Log-out
            </IonButton>
          )}
        </IonButtons>
      </IonHeader>
      <IonContent fullscreen>
        <IonHeader collapse="condense">
          <IonToolbar>
            <IonTitle size="large">Actors</IonTitle>
          </IonToolbar>
        </IonHeader>
        <ExploreContainer name="Tab 2 page" />
      </IonContent>
    </IonPage>
  );
};

export default Actors;

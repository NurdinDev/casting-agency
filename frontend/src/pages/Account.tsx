import React, { useEffect, useState } from "react";
import {
  IonContent,
  IonHeader,
  IonPage,
  IonTitle,
  IonToolbar,
  IonButton,
  IonText,
  IonButtons,
} from "@ionic/react";
import { useAuth0 } from "@auth0/auth0-react";
import Can from "../components/Can";
import { returnTo } from "../constants";

const Account: React.FC = () => {
  const {
    user,
    loginWithRedirect,
    logout,
    isAuthenticated,
    getAccessTokenSilently,
  } = useAuth0();
  const [token, setToken] = useState("");
  const [userMetadata, setUserMetadata] = useState(null);

  useEffect(() => {
    console.log(user);
  }, [user]);

  useEffect(() => {
    const getUserMetadata = async () => {
      const domain = process.env.REACT_APP_AUTH0_DOMAIN;

      try {
        const accessToken = await getAccessTokenSilently();

        setToken(accessToken);

        const userDetailsByIdUrl = `https://${domain}/api/v2/users/${user.sub}/permissions`;

        const metadataResponse = await fetch(userDetailsByIdUrl, {
          headers: {
            Authorization: `Bearer ${accessToken}`,
          },
        });

        const { user_metadata } = await metadataResponse.json();

        console.log({ user_metadata });

        setUserMetadata(user_metadata);
      } catch (e) {
        console.log(e.message);
      }
    };

    getUserMetadata();
  }, [getAccessTokenSilently, user.sub]);

  return (
    <IonPage>
      <IonHeader>
        <IonToolbar>
          <IonTitle>Account</IonTitle>
          <IonButtons slot="secondary">
            {!isAuthenticated ? (
              <IonButton color="secondary" onClick={() => loginWithRedirect()}>
                Login
              </IonButton>
            ) : (
              <IonButton
                color="secondary"
                onClick={() => logout({ returnTo: returnTo })}
              >
                Log-out
              </IonButton>
            )}
          </IonButtons>
        </IonToolbar>
      </IonHeader>
      <IonContent fullscreen>
        <IonHeader collapse="condense">
          <IonToolbar>
            <IonTitle size="large">Account</IonTitle>
          </IonToolbar>
        </IonHeader>
        {user ? (
          <IonText>
            <h2>{user.name}</h2>
            <p>{user.email}</p>
          </IonText>
        ) : null}

        {token ? (
          <>
            <IonText>
              <h2>Active JWT:</h2>
            </IonText>
            <p>{token}</p>
          </>
        ) : null}

        {userMetadata ? (
          <pre>{JSON.stringify(userMetadata, null, 2)}</pre>
        ) : (
          "No user metadata defined"
        )}
      </IonContent>
    </IonPage>
  );
};

export default Account;

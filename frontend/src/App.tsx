import React from "react";
import { Redirect, Route } from "react-router-dom";
import {
  IonApp,
  IonIcon,
  IonLabel,
  IonRouterOutlet,
  IonTabBar,
  IonTabButton,
  IonTabs,
} from "@ionic/react";
import { IonReactRouter } from "@ionic/react-router";
import { ellipse, square, triangle } from "ionicons/icons";
import Movies from "./pages/Movies";
import Actors from "./pages/Actors";
import SingleActor from "./pages/SingleActor";
import Account from "./pages/Account";

/* Core CSS required for Ionic components to work properly */
import "@ionic/react/css/core.css";

/* Basic CSS for apps built with Ionic */
import "@ionic/react/css/normalize.css";
import "@ionic/react/css/structure.css";
import "@ionic/react/css/typography.css";

/* Optional CSS utils that can be commented out */
import "@ionic/react/css/padding.css";
import "@ionic/react/css/float-elements.css";
import "@ionic/react/css/text-alignment.css";
import "@ionic/react/css/text-transformation.css";
import "@ionic/react/css/flex-utils.css";
import "@ionic/react/css/display.css";

/* Theme variables */
import "./theme/variables.css";
import { useAuth0 } from "@auth0/auth0-react";

const App: React.FC = () => {
  const { isLoading, error } = useAuth0();

  if (error) {
    return <div>Oops... {error.message}</div>;
  }

  if (isLoading) {
    return <p>Loading...</p>;
  }

  return (
    <IonApp>
      <IonReactRouter>
        <IonTabs>
          <IonRouterOutlet>
            <Route path="/movies" component={Movies} exact={true} />
            <Route path="/actors" component={Actors} exact={true} />
            <Route path="/actors/:id" component={SingleActor} exact={true} />
            <Route path="/account" component={Account} />
            <Route
              path="/"
              render={() => <Redirect to="/movies" />}
              exact={true}
            />
          </IonRouterOutlet>
          <IonTabBar slot="bottom">
            <IonTabButton tab="movies" href="/movies">
              <IonIcon icon={triangle} />
              <IonLabel>Movies</IonLabel>
            </IonTabButton>
            <IonTabButton tab="actors" href="/actors">
              <IonIcon icon={ellipse} />
              <IonLabel>Actors</IonLabel>
            </IonTabButton>
            <IonTabButton tab="account" href="/account">
              <IonIcon icon={square} />
              <IonLabel>Account</IonLabel>
            </IonTabButton>
          </IonTabBar>
        </IonTabs>
      </IonReactRouter>
    </IonApp>
  );
};

export default App;

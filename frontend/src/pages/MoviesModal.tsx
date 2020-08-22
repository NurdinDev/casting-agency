import {
  IonModal,
  IonHeader,
  IonToolbar,
  IonTitle,
  IonButtons,
  IonButton,
  IonContent,
  IonList,
  IonItemDivider,
  IonTextarea,
  IonItem,
  IonInput,
  IonSelect,
  IonSelectOption,
} from "@ionic/react";
import { Controller, useForm } from "react-hook-form";
import React, { useState, useEffect } from "react";

interface IFormInputs {
  name: string;
  about: string;
  actors: [];
}

const MoviesModal: React.FC<{
  isOpen: boolean;
  actors: any[];
  onSubmit: (data: any) => void;
  onDidDismiss: () => void;
  movie?: any;
  isEdit: boolean;
}> = ({ isOpen, actors, onSubmit, onDidDismiss, movie, isEdit }) => {
  const [showModal, setShowModal] = useState(false);
  const { control, handleSubmit, errors } = useForm<IFormInputs>();

  useEffect(() => {
    setShowModal(isOpen);
  }, [isOpen]);

  return (
    <IonModal
      isOpen={showModal}
      cssClass="my-custom-class"
      onDidDismiss={onDidDismiss}
    >
      <IonHeader translucent>
        <IonToolbar>
          <IonTitle>Add Movie</IonTitle>
          <IonButtons slot="end">
            <IonButton onClick={() => setShowModal(false)}>Close</IonButton>
          </IonButtons>
        </IonToolbar>
      </IonHeader>
      <IonContent fullscreen>
        <form
          onSubmit={handleSubmit(onSubmit)}
          style={{
            width: "50%",
            margin: "auto",
          }}
        >
          <IonList lines="none">
            <IonItemDivider>Name</IonItemDivider>
            <IonItem>
              <Controller
                name="name"
                control={control}
                defaultValue={movie["name"] || ""}
                rules={{ required: true }}
                render={({ onChange, onBlur, value }) => (
                  <IonInput value={value} onIonChange={onChange}></IonInput>
                )}
              />
              {errors.name && <span>This field is required</span>}
            </IonItem>
            <IonItemDivider>About</IonItemDivider>
            <IonItem>
              <Controller
                name="about"
                control={control}
                defaultValue={movie["about"] || ""}
                rules={{ required: true }}
                render={({ onChange, onBlur, value }) => (
                  <IonTextarea
                    value={value}
                    onIonChange={onChange}
                  ></IonTextarea>
                )}
              />
              {errors.about && <span>This field is required</span>}
            </IonItem>
            {actors.length ? (
              <>
                <IonItemDivider>Actors</IonItemDivider>
                <IonItem>
                  <Controller
                    name="actors"
                    control={control}
                    defaultValue={movie["actors"] || []}
                    render={({ onChange, onBlur, value, name }) => (
                      <IonSelect
                        value={value}
                        multiple={true}
                        cancelText="Nah"
                        okText="Okay!"
                        onIonChange={(e) => onChange(e.detail.value)}
                      >
                        {actors.map((actor: any) => (
                          <IonSelectOption
                            key={actor.id}
                            value={{ id: actor.id }}
                          >
                            {actor.name}
                          </IonSelectOption>
                        ))}
                      </IonSelect>
                    )}
                  />
                </IonItem>
              </>
            ) : null}
            <IonItem>
              <IonButton type="submit">{isEdit ? "Edit" : "Submit"}</IonButton>
            </IonItem>
          </IonList>
        </form>
      </IonContent>
    </IonModal>
  );
};

export default MoviesModal;

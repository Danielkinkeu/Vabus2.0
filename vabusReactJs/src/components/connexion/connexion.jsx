import React from "react";
import "./connexion.css";

const Connexion = () => {
  return (
    <div className="PartA">
      <div className="section">
        <div className="article">
          <div className="inscription">
            <h1>Connection</h1>
          </div>

          <div className="api">
            <div className="facebook">
              <i className="fab fa-facebook"></i>
              <span>FACEBOOK</span>
            </div>

            <div className="google">
              <i className="fab fa-google"></i>
              <span>GOOGLE</span>
            </div>

            <div className="apple">
              <i className="fab fa-apple"></i>
              <span>APPLE</span>
            </div>
          </div>

          <p className="choix">OU</p>

          <div className="titre2">
            <span> Connectez-vous avec votre adresse e-mail</span>
          </div>

          <div className="formulaire">
            <div classNameName="form">
              <div className="mail">
                <input
                  type="text"
                  placeholder="votre adresse mail"
                  name="mail"
                  id="imail"
                  required
                />
                <span id="spanmail"></span>
              </div>
              <div className="prenom">
                <input
                  type="text"
                  placeholder="mot de passe"
                  name="prenom"
                  id="password"
                />
                <span id="spanprenom"></span>
              </div>
            </div>

            <p className="soumission">
              <input type="submit" value="Se connecter" />
            </p>

            <p className="ouii" style="padding-top: 10px; margin-left:10px">
              <span>
                Vous n'avez pas de compte ?{" "}
                <a href="/inscription">Inscrivez vous !</a>
              </span>
            </p>
          </div>
        </div>
      </div>
    </div>
  );
};
export default Connexion;

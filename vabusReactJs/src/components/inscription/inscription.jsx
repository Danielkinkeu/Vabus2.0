import React from "react";
import "./inscription.css";

const Inscription = () => {
  return (
    <div className="PartA">
      <div className="section">
        <div className="article">
          <div className="inscription">
            <h1>Inscription</h1>
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
            <span>Inscrivez-vous avec votre adresse e-mail</span>
          </div>

          <div className="formulaire">
            <div className="form" action="traitement.php" method="GET">
              <div className="nom">
                <input
                  type="text"
                  placeholder="votre nom"
                  name="nom"
                  id="name"
                />
                <span id="spannom"></span>
              </div>

              <div className="prenom">
                <input
                  type="text"
                  placeholder="votre prenom"
                  name="prenom"
                  id="pname"
                />
                <span id="spanprenom"></span>
              </div>

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
              <div className="motdepasse">
                <input
                  type="password"
                  placeholder="votre mot de passe"
                  name="mail"
                  id="mdp"
                  required
                />
                <span id="spanmdp"></span>
              </div>

              <div className="conmotdepasse">
                <input
                  type="password"
                  placeholder="confirmer le mot de passe"
                  name="mail"
                  id="cmdp"
                  required
                />
                <span id="spanmdp"></span>
              </div>
              <span className="verif"> </span>
            </div>

            <div className="condition">
              <p className="con-utilisation1">
                <input type="checkbox" name="" id="check" required /> J'ai lu et
                j'accepte les <a href="#">conditions generales d'utilisation</a>{" "}
                et de{" "}
                <a href="">
                  la politique de protection des donnees personelles
                </a>
              </p>

              <p className="soumission">
                <input type="submit" value="S'inscrire" />
              </p>

              <p className="ouii">
                <span>
                  Vous avez deja un compte ?{" "}
                  <a href="connexion.html">Connecter vous !</a>
                </span>
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};
export default Inscription;

import React from "react";
import "./footer.css";

const Footer = () => {
  return (
    <div className="PartC">
      <div className="foo">Vabus a traver l'Afrique</div>

      <div className="footer">
        <div className="footer1">
          <div className="footer">Algerie</div>
          <div className="footer">Maroc</div>
          <div className="footer">Gabon</div>
          <div className="footer">Cote d'ivoire</div>
          <div className="footer">Togo</div>
        </div>
        <div className="footer2">
          <div className="footer">Equatoguinée</div>
          <div className="footer">L'Afrique du Sud</div>
          <div className="footer">Tunisie</div>
          <div className="footer">Benin</div>
          <div className="footer">Senegal</div>
          <div className="footer">RDC</div>
        </div>
        <div className="footer3">
          <div className="footer " style={{ color: "red" }}>
            Partenaires
          </div>
          <div className="footer">Institut St Jean</div>
          <div className="footer">SLKF</div>
          <div className="footer">Yango</div>
        </div>
      </div>
    </div>
  );
};

export default Footer;

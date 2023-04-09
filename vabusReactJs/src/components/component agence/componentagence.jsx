import React from "react";
import "./agence.css";
import bus1 from "../../img/bus2.jpeg";

const ComponentAgence = () => {
  return (
    <div>
      <nav aria-label="breadcrumb">
        <ol className="breadcrumb">
          <li className="breadcrumb-item">
            <a href="/">Home</a>
          </li>
          <li className="breadcrumb-item active" aria-current="page">
            Nom de l'agence
          </li>
        </ol>
      </nav>

      <div className="row">
        <div className="col-12 col-md-4">
          <img
            src={bus1}
            className="img-fluid sticky-top"
            alt="Finex"
            loading="lazy"
          />
        </div>

        <div className="col-12 col-md-8">
          <div className="row">
            <div className="col-12">
              <h1> Finex Voyage </h1>
              <br />
              <p style={{ margin: "15PX;" }}>
                gyefbzh efbbeufbh uhefcfeuf h euf e uefbeu uffbd uecebu
              </p>
              <div className="prix" style={{ display: "flex" }}>
                <div className="card-columns;">
                  <div className="card" style={{ width: " 18em;" }}>
                    <div className="card-body">
                      <h5 className="card-title">
                        <strong> Yaounde - Douala </strong>
                      </h5>
                      <br />
                      8000
                      <br />
                      <a href="/reserver" className="btn btn-warning">
                        Reserver
                      </a>
                    </div>
                  </div>
                </div>

                <div className="card-columns">
                  <div className="card" style={{ width: "18em;" }}>
                    <div className="card-body">
                      <h5 className="card-title">
                        <strong> Yaounde - Douala</strong>
                      </h5>
                      <br />
                      8000
                      <br />
                      <a href="/reserver" className="btn btn-warning">
                        Reserver
                      </a>
                    </div>
                  </div>
                </div>
                <div className="card-columns">
                  <div className="card" style={{ width: "18em;" }}>
                    <div className="card-body">
                      <h5 className="card-title">
                        <strong> Yaounde - Douala</strong>
                      </h5>
                      <br />
                      8000 <br />
                      <a href="/reserver" className="btn btn-warning">
                        f Reserver
                      </a>
                    </div>
                  </div>
                </div>
                <div className="card-columns">
                  <div className="card" style={{ width: "18em" }}>
                    <div className="card-body">
                      <h5 className="card-title">
                        <strong> Yaounde - Douala</strong>
                      </h5>
                      <br />
                      8000
                      <br />
                      <a href="/reserver" className="btn btn-warning">
                        Reserver
                      </a>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div className="row pt-4">
          <div className="col-12">
            <h4>Commentaire</h4>
            Tres belle agence
          </div>
        </div>
      </div>
    </div>
  );
};
export default ComponentAgence;

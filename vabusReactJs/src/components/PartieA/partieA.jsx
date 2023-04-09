import React from "react";
import "./partieA.css";
import Roadd from "./Roadd.jpeg";

const PartA = () => {
  return (
    <div className="row flex-lg-row-reverse align-items-center g-5 py-4 mb-4">
      <div className="col-12 col-lg-6">
        <img
          src={Roadd}
          width="607"
          height="1700px"
          className="d-block mx-lg-auto img-fluid"
          loading="lazy"
          alt="Vabus"
        />
      </div>

      <div className="col-12 col-lg-6">
        <h1 className="display-5 fw-bold mb-3">
          Reserver une place dans un bus, sans vous deplacer
        </h1>
        <p className="lead">
          Nous vous permettons de reserver un voyages avec la possibilité de
          pour reserver un hotel, commander un Yango a un prix unique
        </p>

        <div
          className="d-grid gap-2 d-md-flex justify-content-md-start"
          style={{ color: "red" }}
        >
          <a
            href="../../pages/reserver/reserver"
            className="btn btn-primary btn-dark btn-lg px-4 me-md-2"
          >
            Reserver
          </a>
        </div>
      </div>
    </div>
  );
};

export default PartA;

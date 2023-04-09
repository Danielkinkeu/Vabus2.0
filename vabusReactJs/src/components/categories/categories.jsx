import React from "react";
import "./categories.css";
import Pagecategories from "../../pages/categories.jsx/categories";
import bus1 from "../../img/bus2.jpeg";
import bus2 from "../../img/bus3.jpeg";

import bus4 from "../../img/bus5.jpeg";
import bus6 from "../../img/bus6.jpg";
const Categories = () => {
  return (
    <div>
      <h1 className="pb-4">Explorez les agence</h1>

      <nav aria-label="breadcrumb">
        <ol className="breadcrumb">
          <li className="breadcrumb-item">
            <a href="/">Acceuil</a>
          </li>
          <li className="breadcrumb-item">
            <a href="/">Villes</a>
          </li>
          <li className="breadcrumb-item active" aria-current="page">
            Choissisez la votre Agence
          </li>
        </ol>
      </nav>
      <div className="row row-cols-2 row-cols-lg-5 g-2 g-lg-3">
        <a href="/agence" className="col text-center category__link">
          <div className="category__img category__img--large shadow">
            <img src={bus1} alt="vabus" loading="lazy" />
          </div>
          <div className="pt-1">Touristique Voyage</div>
        </a>

        <a href="/agence" className="col text-center category__link">
          <div className="category__img category__img--large shadow">
            <img src={bus1} alt="vabus" loading="lazy" />
          </div>
          <div className="pt-1">Finex Voyage Mvan</div>
        </a>

        <a href="/agence" className="col text-center category__link">
          <div className="category__img category__img--large shadow">
            <img src={bus2} alt="vabus" loading="lazy" />
          </div>
          <div className="pt-1">General Voyage</div>
        </a>

        <a href="/agence" className="col text-center category__link">
          <div className="category__img category__img--large shadow">
            <img src={bus4} alt="vabus" loading="lazy" />
          </div>
          <div className="pt-1">Buca Voyage</div>
        </a>
        <a href="/agence" className="col text-center category__link">
          <div className="category__img category__img--large shadow">
            <img src={bus6} alt="vabus" loading="lazy" />
          </div>
          <div className="pt-1">Touristique Voyage</div>
        </a>
      </div>
    </div>
  );
};
export default Categories;

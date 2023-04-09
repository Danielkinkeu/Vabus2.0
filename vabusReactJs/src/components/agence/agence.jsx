import React from "react";
import "./agence.css";
import bus1 from "../../img/bus2.jpeg";
import bus2 from "../../img/bus3.jpeg";

import bus4 from "../../img/bus5.jpeg";
import bus6 from "../../img/bus6.jpg";
const Agence = () => {
  return (
    <div>
      <div className="pb-4 pt-4">
        <div className="d-flex mb-2 align-items-center">
          <h2>Yaoundé</h2>
          <a href="/categories" className="ms-auto">
            View More
          </a>
        </div>

        <div className="row row-cols-2 row-cols-lg-5 g-2 g-lg-3">
          <a href="/agence" className="col text-center category__link">
            <div className="category__img category__img--large shadow">
              <img src={bus1} alt="vabus" loading="lazy" />
            </div>
            <div className="pt-1">Touristique Voyage</div>
          </a>

          <a href="/agence" className="col text-center category__link">
            <div className="category__img category__img--large shadow">
              <img src={bus4} alt="vabus" loading="lazy" />
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
              <img src={bus4} alt="vabus" loading="lazy" />
            </div>
            <div className="pt-1">Touristique Voyage</div>
          </a>
        </div>
      </div>

      <div className="pb-4 pt-4">
        <div className="d-flex mb-2 align-items-center">
          <h2>Douala</h2>
          <a href="/categories" className="ms-auto">
            View More
          </a>
        </div>

        <div className="row row-cols-2 row-cols-lg-5 g-2 g-lg-3">
          <a href="/agence" className="col text-center category__link">
            <div className="category__img category__img--large shadow">
              <img src={bus6} alt="vabus" loading="lazy" />
            </div>
            <div className="pt-1">Finex Voyage Mvan</div>
          </a>

          <a href="/agence" className="col text-center category__link">
            <div className="category__img category__img--large shadow">
              <img src={bus1} alt="vabus" loading="lazy" />
            </div>
            <div className="pt-1">General Voyage</div>
          </a>

          <a href="/agence" className="col text-center category__link">
            <div className="category__img category__img--large shadow">
              <img src={bus2} alt="vabus" loading="lazy" />
            </div>
            <div className="pt-1">Buca Voyage</div>
          </a>
          <a href="/agence" className="col text-center category__link">
            <div className="category__img category__img--large shadow">
              <img src={bus6} alt="vabus" loading="lazy" />
            </div>
            <div className="pt-1">Touristique Voyage</div>
          </a>
          <a href="/agence" className="col text-center category__link">
            <div className="category__img category__img--large shadow">
              <img src={bus4} alt="vabus" loading="lazy" />
            </div>
            <div className="pt-1">Touristique Voyage</div>
          </a>
        </div>
      </div>

      <div className="pb-4 pt-4">
        <div className="d-flex mb-2 align-items-center">
          <h2>Baffoussam</h2>
          <a href="/categories" className="ms-auto">
            View More
          </a>
        </div>

        <div className="row row-cols-2 row-cols-lg-5 g-2 g-lg-3">
          <a href="/agence" className="col text-center category__link">
            <div className="category__img category__img--large shadow">
              <img src={bus1} alt="vabus" loading="lazy" />
            </div>
            <div className="pt-1">Finex Voyage</div>
          </a>

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
            <div className="pt-1">General Voyage</div>
          </a>

          <a href="/agence" className="col text-center category__link">
            <div className="category__img category__img--large shadow">
              <img src={bus1} alt="vabus" loading="lazy" />
            </div>
            <div className="pt-1">Buca Voyage</div>
          </a>
          <a href="/agence" className="col text-center category__link">
            <div className="category__img category__img--large shadow">
              <img src={bus1} alt="vabus" loading="lazy" />
            </div>
            <div className="pt-1">Touristique Voyage</div>
          </a>
        </div>
      </div>
    </div>
  );
};
export default Agence;

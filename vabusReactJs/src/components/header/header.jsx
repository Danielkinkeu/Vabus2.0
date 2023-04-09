import React from "react";
import "./hearder.css";

const Header = () => {
  return (
    <div className="container-xxl px-md-5 bg-white shadow-lg">
      <header className="d-flex flex-wrap align-items-center justify-content-center justify-content-md-between py-3 mb-4 border-bottom">
        <div className="slogan">
          <a
            href="/"
            className="d-flex align-items-center col-md-3 mb-2 mb-md-0 text-dark text-decoration-none"
          >
            <span> Vabus</span>
          </a>
        </div>

        <ul className="nav col-12 col-md-auto mb-2 justify-content-center mb-md-0">
          <li>
            <a href="/pages/Home/Home" className="nav-link px-2 link-secondary">
              Accueil
            </a>
          </li>
          <li>
            <a
              href="/pages/about/about"
              className="nav-link px-2 link-secondary"
            >
              A Propos
            </a>
          </li>
          <li>
            <a
              href="/pages/connexion/connexion"
              className="nav-link px-2 link-secondary"
            >
              Connexion
            </a>
          </li>
        </ul>

        <div className="col-md-3 text-end">
          <form method="POST" action="/search">
            <input
              type="search"
              name="searchTerm"
              className="form-control"
              placeholder="Search..."
              aria-label="Search"
            />
          </form>
        </div>
      </header>
    </div>
  );
};
export default Header;

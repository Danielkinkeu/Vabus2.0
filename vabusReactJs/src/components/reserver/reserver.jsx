import React from "react";
import "./reserver.css";

const Reserver = () => {
  return (
    <div className="PartA" style={{ height: "650px" }}>
      <div className="section">
        <div className="article">
          <div className="formulaire">
            <span className="dddd">Ville de depart</span>
            <select name="ville" id="" className="ville">
              <option value="">Baffoussam</option>
              <option value="">Douala</option>
              <option value="">Yaounde</option>
              <option value="">Ngaoundere</option>
              <option value="">Bafia</option>
              <option value="">Edea</option>
              <option value="">Foumban</option>
            </select>
            <span className="dddd">Ville de destination</span>
            <select name="ville" id="" className="villes">
              <option value="">Baffoussam</option>
              <option value="">Douala</option>
              <option value="">Yaounde</option>
              <option value="">Ngaoundere</option>
              <option value="">Bafia</option>
              <option value="">Edea</option>
              <option value="">Foumban</option>
            </select>
            <span className="dddd">Nombre de places</span>
            <input
              type="number"
              name="mail"
              id="nplace"
              className="nmplace"
              required
            />
            <span id="spannum"></span>
            <span className="dddd">Date du voyage</span>
            <div className="date" style={{ margin: "20PX;" }}>
              <select name="Jours" id="">
                <option value="">Jour</option>
                <option value="">01</option>
                <option value="">02</option>
                <option value="">03</option>
                <option value="">04</option>
                <option value="">05</option>
                <option value="">06</option>
                <option value="">07</option>
                <option value="">08</option>
                <option value="">09</option>
                <option value="">10</option>
                <option value="">11</option>
                <option value="">12</option>
                <option value="">13</option>
                <option value="">14</option>
                <option value="">15</option>
                <option value="">16</option>
                <option value="">17</option>
                <option value="">18</option>
                <option value="">19</option>
                <option value="">20</option>
                <option value="">20</option>
                <option value="">21</option>
                <option value="">22</option>
                <option value="">23</option>
                <option value="">24</option>
                <option value="">25</option>
                <option value="">26</option>
                <option value="">27</option>
                <option value="">28</option>
                <option value="">29</option>
                <option value="">30</option>
                <option value="">31</option>
              </select>

              <select name="Mois" id="">
                <option value="">Mois</option>
                <option value="">Janvier</option>
                <option value="">Fevrier</option>
                <option value="">Mars</option>
                <option value="">Avril</option>
                <option value="">Mai</option>
                <option value="">Juin</option>
                <option value="">Juillet</option>
                <option value="">Aout</option>
                <option value="">Septembre</option>
                <option value="">Octobre</option>
                <option value="">Novembre</option>
                <option value="">Decembre</option>
              </select>

              <select name="Année" id="">
                <option value="">Année</option>
                <option value="">1990</option>
                <option value="">1991</option>
                <option value="">1992</option>
                <option value="">1993</option>
                <option value="">1994</option>
                <option value="">1995</option>
                <option value="">1996</option>
                <option value="">1997</option>
                <option value="">1998</option>
                <option value="">1999</option>
                <option value="">2000</option>
                <option value="">2001</option>
                <option value="">2002</option>
                <option value="">2003</option>
                <option value="">2004</option>
                <option value="">2005</option>
                <option value="">2006</option>
                <option value="">2007</option>
                <option value="">2008</option>
                <option value="">2009</option>
                <option value="">2010</option>
                <option value="">2011</option>
                <option value="">2012</option>
                <option value="">2013</option>
                <option value="">2014</option>
                <option value="">2015</option>
                <option value="">2016</option>
                <option value="">2017</option>
                <option value="">2018</option>
                <option value="">2019</option>
                <option value="">2020</option>
                <option value="">2021</option>
              </select>
            </div>
          </div>

          <div className="sub" style={{ display: "flex" }}>
            <div className="d-grid gap-2 d-md-flex justify-content-md-start">
              <a
                href="/Reserver"
                className="btn btn-primary btn-red btn-lg px-10 me-md-2"
              >
                Reserver
              </a>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};
export default Reserver;

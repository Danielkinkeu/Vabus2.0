import React from "react";
import "./Home.css";
import Header from "../../components/header/header";
import PartA from "../../components/PartieA/partieA";
import Footer from "../../components/footer/footer";
import Agence from "../../components/agence/agence";
const Home = () => {
  return (
    <div>
      <Header />

      <PartA />
      <Agence />
      <Footer />
    </div>
  );
};
export default Home;

import React from "react";
import "./Home.css";
import Header from "../../components/header/header";
import PartA from "../../components/PartieA/partieA";
import Footer from "../../components/footer/footer";
import Agence from "../../components/agence/agence";
// import AgenceList from './AgenceList';
// import AgenceList from "../../AgenceList";
const Home = () => {
  return (
    <div>
      <Header />

      <PartA />
      <Agence />
      {/* <AgenceList /> */}
      <Footer />
    </div>
  );
};
export default Home;

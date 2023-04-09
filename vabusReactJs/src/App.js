import{ 
    BrowserRouter,
    Routes,
    Route,
} from "react-router-dom"

import Home from "./pages/Home/Home";
import Pagecategories from "./pages/categories.jsx/categories";
import PageAgence from "./pages/agence/agence";
import PageConnexion from "./pages/connexion.jsx/connexion";
import PageReserver from "./pages/reserver.jsx/reserver";
import PageInscription from "./pages/inscription.jsx/inscription";


function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home/>} />
        <Route path="/categories" element={<Pagecategories />} />
        <Route path="/agence" element={<PageAgence />} />
        <Route path="/connexion" element={<PageConnexion />} />
        <Route path="/inscription" element={<PageInscription/>} />
        <Route path="/reserver" element={<PageReserver />} />
        </Routes>
    </BrowserRouter>
  );
}

export default App;

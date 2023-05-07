// import React from "react";
// class AgenceList extends React.Component {
//     constructor(props) {
//       super(props);
//       this.state = {
//         error: null,
//         isLoaded: false,
//         agences: []
//       };
//     }
  
//     componentDidMount() {
//       fetch("http://127.0.0.1:8000/api/gestionAgences/agenceList")
//         .then(res => res.json())
//         .then(
//           (result) => {
//             console.log(result);
//             this.setState({
//               isLoaded: true,
//               agences: result
//             });
//           },
//           // Note: it's important to handle errors here
//           // instead of a catch() block so that we don't swallow
//           // exceptions from actual bugs in components.
//           (error) => {
//             this.setState({
//               isLoaded: true,
//               error
//             });
//           }
//         )
//     }
  
//     render() {
//       const { error, isLoaded, agences } = this.state;
//       if (error) {
//         return <div>Error: {error.message}</div>;
//       } else if (!isLoaded) {
//         return <div>Loading...</div>;
//       } else {
//         return (
//           <ul>
//             {agences?.results?.map(item => (
//               <li key={item.id}>
//                 {item.name} {item.picture} {item.siege} {item.telephone} 
//                 {item.description} {item.published}
//               </li>
//             ))}
//           </ul>
//         );
//       }
//     }
//   }

// export default AgenceList;  
import axios from "axios";
import React, { Component } from 'react';
import './App.css';
class App extends Component {
  state = {
    data:[],
  };

  componentDidMount() {
    let data;
    axios.get("http://localhost:8000/api/").then((res) => {
      data = res.data;
      this.setState({ data:data });
    })
    .catch((error) => {
      console.log(error);
    })
  }

  render() {
    return (
      <div>
      <header>Individual Data Testing Backend Fetch</header>
      <hr></hr>
      {this.state.data.map((Individual,id) => (
        <div key={id}>
          <div>
          <h1>{Individual.first_name}</h1>
          <h1>{Individual.lastname}</h1>
          <h2>{Individual.email}</h2>
          </div>
          </div>
      ))}
      </div>
    );
  }
}
export default App;
import './App.css';
import React, { useState, useEffect } from 'react';
import { server } from '../Server';
import { GLOBALS } from './Constants';
import Gantt from './Gantt';

const connect = server();
const [databaseValues, setDatabaseValues] = useState({});

// Function that fetches DB data into a state variable
function Connect() {
  let requestOptions = {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(DB_name.key)
  }
  fetch(
    connect + GLOBALS.ROUTE_GET_ALL, requestOptions
  )
    .then(response => response.json())
    .then(json => {
      setDatabaseValues(json);
    })
    .catch(error => {
      console.log(error)
      setIsInitError(true);
    })
  return console.log("DB connection successful")
}

function App() {
  Connect();
  ganttData = databaseValues.tasks;
  return (
    <div className="App">
      <header className="App-header">
        <p>
          Model Full Stack App with DHTMLX Gantt
        </p>
        <Gantt
          tasks={ganttData}
        />
      </header>
    </div>
  );
}

export default App;

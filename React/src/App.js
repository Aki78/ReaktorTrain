import React, { useState, useEffect } from 'react';
import './App.css';
import Points from './Components/Points';
import NaughtyList from './Components/NaughtyList';

function App() {
  const [list, setList] = useState([]);
  const [filteredList, setFilteredList] = useState([]);

  async function fetchList() {
    try {
      const response = await fetch('http://aki78.pythonanywhere.com/fetch_recent_naughty_pilots');
      const data = await response.json();
      setList(data);
      console.log("data: ", data);
    } catch (error) {
      console.error(error);
    }
  }
// Fetching list every 1.9 seconds. Must be below 2 seconds for real time
  useEffect(() => {
    const interval = setInterval(fetchList, 1900);
    return () => clearInterval(interval);
  }, []);


  return (
    <div className="App">
      <h2>Zone Entered</h2>
      <Points list={list} />
      <h1>List of contact information from past 10 min.</h1>
      <NaughtyList list={list} />
    </div>
  );
}

export default App;

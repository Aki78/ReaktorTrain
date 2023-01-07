import React, { useState, useEffect } from 'react';
import "./Points.css"
import getColor from "./utils.js"

function Points() {
  const [positionList, setPositionList] = useState([]);

    async function fetchData() {
      let response = await fetch('http://localhost:12345/fetch_recent_naughty_pilots');
      let data = await response.json();
      // console.log(data)
      setPositionList(data);
    }


  // Call the function every 1.9 seconds
  useEffect(() => {
    const interval = setInterval(fetchData, 1900);
    return () => clearInterval(interval);
  }, []);




  return (
    <div className="container">
      {positionList.map(point => (
        <div
          key={point.X}
          className="point"
          style={{
            left: point.X/1000,
            top: point.Y/1000,
	    backgroundColor: getColor(point.pilot_id)
          }}
	                data-tooltip={point.firstName + " " + point.lastName}
          onMouseOver={e => e.currentTarget.classList.add('pointHover')}
          onMouseOut={e => e.currentTarget.classList.remove('pointHover')}
        />
      ))}
    </div>
  );
}

export default Points;


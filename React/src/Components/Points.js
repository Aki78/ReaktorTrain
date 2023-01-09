import React, { useState, useEffect } from 'react';
import "./Points.css"
import getColor from "./utils.js"

function Points({list}) {
  // You can simply use "list" instead of "positionList"? You don't need an internal state for list, since you are just using the original variable.
  // Also remove the useEffect.
  const [positionList, setPositionList] = useState([]);

  useEffect(() => {
    setPositionList(list)
  }, [list]);

  return (
    <div className="container">
      {positionList.map(point => (
        <div
          key={point.X}
          className="point"
          style={{
            left: point.X/1000 - 500/4,
            top: point.Y/1000 - 500/4,
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


import React, { useState, useEffect } from 'react';

function Points({ points }) {
  const [positionList, setPositionList] = useState([]);

  useEffect(() => {
    async function fetchData() {
      const response = await fetch('http://example.com/points');
      const data = await response.json();
      setPositionList(data);
    }

    fetchData();
  }, []);

  return (
    <div className="container">
      {positionList.map(point => (
        <div
          key={point.id}
          className="point"
          style={{
            left: point.x,
            top: point.y,
          }}
          onMouseOver={e => e.currentTarget.classList.add('pointHover')}
          onMouseOut={e => e.currentTarget.classList.remove('pointHover')}
        />
      ))}
    </div>
  );
}

export default Points;

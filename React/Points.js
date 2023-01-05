import React from 'react';

function Points({ points }) {
  const styles = {
    container: {
      width: '500px',
      height: '500px',
      border: '1px solid black',
      position: 'relative',
    },
    point: {
      position: 'absolute',
      width: '10px',
      height: '10px',
      borderRadius: '50%',
      backgroundColor: 'red',
    },
  };

  return (
    <div style={styles.container}>
      {points.map(point => (
        <div
          key={point.id}
          style={{
            ...styles.point,
            left: point.x,
            top: point.y,
          }}
        />
      ))}
    </div>
  );
}

export default Points;


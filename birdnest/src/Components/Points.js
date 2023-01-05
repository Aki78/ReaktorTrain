import React from 'react';

function Points({ points }) {
  const styles = {
    container: {
      width: '400px',
      height: '400px',
      border: '1px solid black',
      position: 'relative',
    },
    point: {
      position: 'absolute',
      width: '20px',
      height: '20px',
      borderRadius: '50%',
      backgroundColor: 'red',
      transition: 'box-shadow 0.5s ease',
    },
    pointHover: {
      boxShadow: '0 0 10px 5px rgba(0, 0, 0, 0.5)',
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
          onMouseOver={e => e.currentTarget.style.cssText += styles.pointHover.cssText}
          onMouseOut={e => e.currentTarget.style.cssText = styles.point.cssText}
        />
      ))}
    </div>
  );
}

export default Points;


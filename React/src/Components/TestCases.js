import Points from './Points';

const points = [
  { id: 1, x: 50, y: 50 },
  { id: 2, x: 100, y: 100 },
  { id: 3, x: 150, y: 150 },
];

function App() {
  return <Points points={points} />;
}


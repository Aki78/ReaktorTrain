// Instead of this kind of a test component that does not get tested in any test suite,
// odeally each component would have some kind of a unit test using testing-library that you had used in App.test.js.
// But might be an overkill for this assignment, not sure.
import Points from './Points';

const points = [
  { id: 1, x: 50, y: 50 },
  { id: 2, x: 100, y: 100 },
  { id: 3, x: 150, y: 150 },
];

function App() {
  return <Points points={points} />;
}


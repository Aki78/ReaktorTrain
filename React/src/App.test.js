/* This test file is probably a leftover from some initial project. It is testing that
 * the text "learn react" is found in the app, which should not work..? Simply remove
 * if you don't want any testing. If you want to add tests (might be a good idea, you can
 * simply modify this file and see that the tests pass)
 * /
import { render, screen } from '@testing-library/react';
import App from './App';

test('renders learn react link', () => {
  render(<App />);
  const linkElement = screen.getByText(/learn react/i);
  expect(linkElement).toBeInTheDocument();
});

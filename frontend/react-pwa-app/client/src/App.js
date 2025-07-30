import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Splash from './Splash';
import StartPage from './StartPage';

import HomeScreen from './HomeScreen';
import CameraScreen from './CameraScreen'; 
import LoadingPage from './LoadingPage';
import SummaryPage from './SummaryPage';
import RecordPage from './RecordPage';


function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Splash />} />
        <Route path="/start" element={<StartPage />} />
        <Route path="/home" element={<HomeScreen />} />
        <Route path="/camera" element={<CameraScreen />} />
        <Route path="/load" element={<LoadingPage />} />
        <Route path="/summary" element={<SummaryPage />} />
        <Route path="/record" element={<RecordPage />} />
      </Routes>
    </BrowserRouter>
  );
}
export default App;

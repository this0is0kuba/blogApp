import Navbar from './layout/Navbar';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import Home from './main/Home';
import BlogSearcher from './main/BlogSearcher';

function App() {
  return (
    <div className="App">
        <Navbar/>

        <main className='container text-light rounded'>

          <BrowserRouter>
            <Routes>

              <Route path='/' element={<Home/>}></Route>
              <Route path='/blogs' element={<BlogSearcher/>}></Route>

            </Routes>
          </BrowserRouter>

        </main>
    </div>
  );
}

export default App;

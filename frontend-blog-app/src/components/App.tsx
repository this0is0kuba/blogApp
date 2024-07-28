import Navbar from './layout/Navbar';
import {Route, Routes } from 'react-router-dom';
import Home from './main/Home';
import BlogSearcher from './main/BlogSearcher';
import BlogPage from './main/BlogPage';

function App() {
  return (
    <div className="App">
        <Navbar/>

        <main className='container text-light rounded'>

            <Routes>

              <Route path='/' element={<Home/>}></Route>
              <Route path='/blogs' element={<BlogSearcher/>}></Route>
              <Route path='/blogs/:id' element={<BlogPage/>} ></Route>

            </Routes>

        </main>
    </div>
  );
}

export default App;

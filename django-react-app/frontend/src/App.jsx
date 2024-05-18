/* eslint-disable no-unused-vars */
import { useState } from 'react'
import Search from './Components/Search'
import AddTodo from './Components/AddTodo'
import PredictForm from './Components/PredictForm'
import Header from './Components/Header'

function App() {

  return (
    <>
    <Header />
     <h1>Hello World</h1>
     <h2>Django</h2>
     <h3>React</h3>
    <Search />
    <AddTodo />
    <br />
    <PredictForm />
    </>
  )
}

export default App

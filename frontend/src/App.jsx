import React, { useState, useEffect } from "react";
import axios from "axios";

export default function App() {
  const [todos, setTodos] = useState([]);
  const [title, setTitle] = useState('');
  const [search, setSearch] = useState('');
  const [page, setPage] = useState(1);
  const limit = 5

  const fetchTodos = async () => {
    try {
      const params = {
        search: search || undefined,
        skip: (page - 1) * limit,
        limit,
      };
      const res = await axios.get("http://localhost:8000/todo/filter", { params });
      setTodos(res.data);
    } catch (error) {
      console.error("Error fetching todos:", error);
    }
  };

  const createTodo = async () => {
    if (!title.trim()) return;
    await axios.post("http://localhost:8000/todo/", { title });
    setTitle('');
  };

  useEffect(() => {
    fetchTodos();
  }, [search, page]);

  return (
    <div className="p-20 font-mono max-w-2xl mx-auto">
      <h2 className="text-8xl text-center mb-6">Todo App</h2>

      <div className="flex justify-between gap-2 mb-6">
        <input 
          className="p-2 rounded border border-black mt-5 w-full" 
          type="text" 
          value={title} 
          onChange={e => setTitle(e.target.value)} 
          placeholder="New todo" 
        />
        <button 
          className="p-2 rounded border border-black mt-5 ml-4 hover:bg-black hover:text-white" 
          onClick={createTodo}
        >
          Add
        </button>
      </div>

      <div className="flex flex-col sm:flex-row gap-2 mb-4">
        <input 
          className="p-2 border rounded w-full" 
          type="text" 
          value={search}
          onChange={(e) => setSearch(e.target.value)}
          placeholder="Search todos..."
        />
      </div>
      
      <div className="pl-10 mt-8 border border-black rounded max-w-xl mx-auto text-left"> 
        <ul className="divide-y divide-gray-300">
        {
          todos.map(todo => 
            <li 
              key={todo.id}
              className="py-3 px-4 hover:bg-gray-100 cursor-pointer transition-colors duration-200 rounded"
            >
              {todo.title}
            </li>
          )
        }
        </ul>
      </div>

      <div className="flex justify-between mt-6">
        <button
          className="px-4 py-2 border rounded disabled:opacity-50"
          onClick={() => setPage((p) => Math.max(1, p - 1))}
          disabled={page === 1}
        >
          Previous
        </button>
        <span className="px-4 py-2 border rounded">{page}</span>
        <button
          className="px-4 py-2 border rounded"
          onClick={() => setPage((p) => p + 1)}
        >
          Next
        </button>
      </div>
    </div>
  );
}
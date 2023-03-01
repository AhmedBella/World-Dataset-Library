'use client'

import React from "react";
import Logo from "../components/images/Logo.png";
import Image from "next/image";


const Header = () => {
  const [searchText, setSearchText] = React.useState("");

  function handleChange(event) {
    setSearchText(event.target.value);
  }
  return (
    <div className="bg-black w-full top-0 sticky z-10 scroll-pt-12 p-2 px-5 flex">
      <div>
        <Image
          className="cursor-pointer"
          src={Logo}
          width={130.05}
          height={43.2}
        />
      </div>
      <div className="w-1/3 bg-gray-300 rounded-md items-center justify-center mx-auto">
        <div className="flex items-center border-gray-500">
          <input
            className=" bg-transparent border-none w-full text-gray-700 py-1 px-2"
            type="text"
            placeholder="What are we looking for?"
            value={searchText}
            onChange={handleChange}
          />
          <button
            className="flex-shrink-0 bg-gray-500 hover:bg-gray-700 border-gray-500 hover:border-gray-700 text-sm border-4 text-white py-1 px-1 rounded"
            type="submit"
          >
            Go
          </button>
        </div>
      </div>
      <div className="inline-flex items-center justify-center space-x-4">
        <div className="text-white">Log In</div>
        <div className="text-white">Sign Up</div>
      </div>
    </div>
  );
};

export default Header;

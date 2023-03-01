import Header from "../components/Header";
import background from "../components/images/background.png";

export default function Home() {
  return (
    <div>
      <Header />
      <div
        style={{
          backgroundImage: `url(${background.src})`,
        }}
        className="bg-black"
      >
        <div className="w-2/3 mx-auto">
          <h1 className="flex items-center justify-center text-5xl py-32 font-bold text-white">
            Discover the&nbsp;<span className="text-cyan-500">Power</span>
            &nbsp;of
            <span className="text-cyan-500">&nbsp;Data</span>
          </h1>
          <div className="flex flex-col text-white text-xl items-center justify-center text-center">
            At WDL, we believe in the power of data. That's why we've curated a
            large collection of high-quality datasets to help businesses and
            individuals make informed decisions. Explore our datasets now and
            discover insights that drive growth.
          </div>
          <div className="flex w-1/2 mx-auto py-20">
            <input
              id="email"
              type="email"
              className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
              placeholder="Email address"
            />
            <button
              className="flex-shrink-0 bg-cyan-500 text-sm text-white py-1 px-1 rounded"
              type="submit"
            >
              Start your journey
            </button>
          </div>
          <h1 className="flex items-center justify-center text-4xl text-center py-20 font-bold text-white">
            We have exactly what you are looking for
          </h1>
          <div className="flex flex-col text-white text-xl items-center justify-center text-center py-10">
            We're dedicated to providing a comprehensive collection of
            high-quality datasets for researchers, data scientists, and
            developers. Our goal is to make it easier for you to access the data
            you need to train your models, perform research, or build
            applications.
          </div>
        </div>
      </div>
    </div>
  );
}

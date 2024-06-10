export default function Widget() {
    return (
        <div className="flex items-center justify-center min-h-screen bg-gradient-to-r from-green-200 to-teal-500">
          <div className="bg-white dark:bg-zinc-800 p-8 rounded-lg shadow-lg max-w-md w-full">
            <h2 className="text-center text-2xl font-bold mb-6">SIGN UP</h2>
            <form className="space-y-4">
              <div className="relative">
                <input type="text" placeholder="Name" className="w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-teal-500 dark:bg-zinc-700 dark:border-zinc-600">
                <span className="absolute inset-y-0 right-4 flex items-center">
                  <img src="https://placehold.co/20x20" alt="user icon" undefinedhidden="true">
                </span>
              </div>
              <div className="relative">
                <input type="email" placeholder="Email" className="w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-teal-500 dark:bg-zinc-700 dark:border-zinc-600">
                <span className="absolute inset-y-0 right-4 flex items-center">
                  <img src="https://placehold.co/20x20" alt="email icon" undefinedhidden="true">
                </span>
              </div>
              <div className="relative">
                <input type="password" placeholder="Password" className="w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-teal-500 dark:bg-zinc-700 dark:border-zinc-600">
                <span className="absolute inset-y-0 right-4 flex items-center">
                  <img src="https://placehold.co/20x20" alt="lock icon" undefinedhidden="true">
                </span>
              </div>
              <div className="flex items-center">
                <input type="checkbox" id="remember" className="h-4 w-4 text-teal-500 focus:ring-teal-400 border-zinc-300 rounded">
                <label htmlFor="remember" className="ml-2 block text-sm text-zinc-900 dark:text-zinc-300">Remember me</label>
              </div>
              <button type="submit" className="w-full bg-teal-500 text-white py-2 rounded-lg font-semibold hover:bg-teal-600 focus:outline-none focus:ring-2 focus:ring-teal-400">Get Started</button>
            </form>
          </div>
        </div>
    )
}
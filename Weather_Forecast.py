import requestsimport tkinter as tkfrom tkinter import messageboximport json# ConstantsAPI_KEY = "your_openweathermap_api_key"  # Replace with your OpenWeatherMap API keyBASE_URL = "http://api.openweathermap.org/data/2.5/weather"# Fetch weather datadef fetch_weather(city):    try:        params = {            'q': city,            'appid': API_KEY,            'units': 'metric'        }        response = requests.get(BASE_URL, params=params)        data = response.json()        if data.get("cod") != 200:            messagebox.showerror("Error", data.get("message", "Failed to fetch weather data"))            return None        return {            "temperature": data["main"]["temp"],            "humidity": data["main"]["humidity"],            "wind_speed": data["wind"]["speed"],            "conditions": data["weather"][0]["description"],            "local_time": data["dt"]  # Timestamp, needs conversion        }    except Exception as e:        messagebox.showerror("Error", str(e))        return None# Save favorite locationsdef save_favorite_location(city):    try:        with open("favorites.json", "r") as file:            favorites = json.load(file)    except FileNotFoundError:        favorites = []    if city not in favorites:        favorites.append(city)    with open("favorites.json", "w") as file:        json.dump(favorites, file)    messagebox.showinfo("Success", f"{city} added to favorites")# Load favorite locationsdef load_favorite_locations():    try:        with open("favorites.json", "r") as file:            return json.load(file)    except FileNotFoundError:        return []# GUI Setupdef weather_app():    def search_weather():        city = city_entry.get()        weather_data = fetch_weather(city)        if weather_data:            result_label.config(                text=(                    f"Temperature: {weather_data['temperature']} °C\n"                    f"Humidity: {weather_data['humidity']}%\n"                    f"Wind Speed: {weather_data['wind_speed']} m/s\n"                    f"Conditions: {weather_data['conditions']}"                )            )    def add_to_favorites():        city = city_entry.get()        if city:            save_favorite_location(city)    def show_favorites():        favorites = load_favorite_locations()        if favorites:            messagebox.showinfo("Favorites", "\n".join(favorites))        else:            messagebox.showinfo("Favorites", "No favorite locations saved.")    # Main window    window = tk.Tk()    window.title("Weather Forecast App")    tk.Label(window, text="Enter City:").pack(pady=5)    city_entry = tk.Entry(window)    city_entry.pack(pady=5)    tk.Button(window, text="Search Weather", command=search_weather).pack(pady=5)    tk.Button(window, text="Add to Favorites", command=add_to_favorites).pack(pady=5)    tk.Button(window, text="Show Favorites", command=show_favorites).pack(pady=5)    result_label = tk.Label(window, text="", justify=tk.LEFT)    result_label.pack(pady=10)    window.mainloop()if __name__ == "__main__":    weather_app()
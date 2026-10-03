def estimate_hike_time (distance, elevation_gain):
    time =  (distance/2) + (elevation_gain / 1000*0.5)
    return time
  
def display_results(matching_trails, estimated_times):
    if len (matching_trails) > 0:
        print ("Trails matching your plan:")
        for i in range(len(matching_trails)):
            print(f"{matching_trails[i]} {estimated_times[i]: .2f} hours")
    else:
        print("No trails match your hiking plan.")
        print(f"Matching trails: {len(matching_trails)}")
  
def main():
    print("Trail Hike Planner")
  
    max_time = float(input("Maximum hiking time (hours): "))
    desired_difficulty = input("Desired difficulty (Easy, Moderate, Hard): ")

    matching_trails = []
    estimated_times = []

    with open("trails.csv", "r", encoding="utf-8") as file:
        file.readline()
        for line in file:
            clean_line = line.strip()
            if not clean_line:
                continue
            
            fields = line.strip().split(",")
            trail_name = fields[0]
            distance = float(fields[1])
            elevation_gain = float(fields[2])
            difficulty = fields[3]
            
   
            hike_time = estimate_hike_time(distance, elevation_gain)
        
        #for index in range(len(fields[0])):
            #print(difficulty)
            if difficulty == desired_difficulty :
                
                matching_trails.append(trail_name)
                estimated_times.append(hike_time)
    display_results(matching_trails,estimated_times)
if __name__ == "__main__":
    main()


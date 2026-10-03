# Kelvon-S-ENGT102-HW3
A program that will read trail data from a CSV file, calculate estimated hiking times, and identify trails that fit a user’s hiking plan
Function Estimate_hike_time(distance, elevation_gain)
        RETURN (distance / 2) + (elevation_gain / 1000 * 0.5)
Function Display_results(matching_trails, estimated_times)
    IF matching_trails is not empty THEN
        DISPLAY "Trails matching your plan:"
        FOR i FROM 0 TO length of matching_trails - 1
            DISPLAY matching_trails[i] AND estimated_times[i] formatted to 2 decimal places
        ELSE
            DISPLAY "No trails match your hiking plan."
        END IF
          DISPLAY "Matching trails: " + length of matching_trails
    END FUNCTION
    MAIN PROGRAM
        DISPLAY "Trail Hike Planner"
        PROMPT user for max_time as FLOAT
        PROMPT user for desired_difficulty as STRING

        CREATE empty list matching_trails
        CREATE empty list estimated_times

        OPEN "src/trails.csv" for reading
            READ and discard heading line

            FOR EACH line IN file DO
                STRIP whitespace from line
                IF line is empty THEN
                    CONTINUE to next line
                END IF
                SPLIT line by comma INTO fields
                SET trail_name = fields[0]
                SET distance = CONVERT fields[1] TO FLOAT
                SET elevation_gain = CONVERT fields[2] TO FLOAT
                SET difficulty = STRIP whitespace from fields[3]
                CALL estimate_hike_time(distance, elevation_gain) RETURNING hike_time
                IF difficulty EQUALS desired_difficulty AND hike_time <= max_time THEN
                    APPEND trail_name TO matching_trails
                    APPEND hike_time TO estimated_times
        CLOSE file
        CALL display_results(matching_trails, estimated_times)
    END MAIN PROGRAM

    Testing Cases

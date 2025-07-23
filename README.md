# RdLib Library for Rd03d and HLK-LD2450 for raspberrypi

For now library is using only serial communication with these radars. 
Might be necessary to set temporarily permission to the serial port:
- sudo chmod 777 /dev/ttyS0

How to install that library?
- pip install RdLib

Whole library is preconfigured to both radar. Just plug&play
But to be specific here is documentation about implementation: 

-Basic implementation  without any configuration

    from RdLib.Rd import Rd 
    rd = Rd()
    
    print(rd.get_angle())
        """
        Calculates the angle between the radar and the detected object in degrees.

        Returns:
            float: Angle in degrees.
        """
    
    print(rd.get_coordinate())
        """
        Reads radar data and returns the 2D coordinates of the detected object.

        Returns:
            tuple: (x, y) coordinates in meters.
        """
    
    print(rd.OutputDump())
        """
        Returns a full snapshot of radar data.

        Returned values:
            - x (float): X coordinate of the object
            - y (float): Y coordinate of the object
            - distance (float): Converted distance from the radar to the object
            - angle (float): Angle to the object in degrees
            - detection_mode (float): Current radar detection mode
            - raw_distance (float): Raw distance (before conversion)

        Returns:
            tuple: (x, y, distance, angle, detection_mode, raw_distance)
        """
    
    print(rd.get_distance())
        """
        Reads radar data and calculates the distance to the detected object.

        Returns:
            float: Distance to the object in meters.
        """
    
    print(rd.Kalman_Test(100,1,5,"Test2","Test2"))
         """
        Runs a Kalman filter test on distance measurements and visualizes the results.

        Parameters:
        - true_length (float): Expected distance in cm (used as a reference line on the chart).
        - measure_frequency (float): Delay between measurements in seconds.
        - quantity_measure (int): Number of total measurements.
        - chart_comment (str): Title of the chart.
        - file_name (str): Name used to save CSV and chart image.

        Behavior:
        - Collects distance measurements (raw and filtered).
        - Plots real-time updates of both raw and Kalman-filtered data.
        - Saves data to CSV and chart to PNG if configured to do so.
        """
    
    print(rd.Calibrate_Kalman())
            """
        That function gives you raw data from radar compared to the filtered by kalman.
        Important you must turn on kalman by config.set(Kalman=True)

        Returns:
            tuple: A tuple containing two sub-tuples:
                - (distance_raw_x, distance_raw_y): Raw (unfiltered) distance values.
                - (distance_filtered_x, distance_filtered_y): Filtered distance values.
        """
-Advanced implementation with config.
Example:

      from RdLib.Rd import Rd 
      from RdLib.config import config

      
      #Example of Entry Configuration
      config.set(Kalman_Save_csv=False)
      config.set(Kalman=True)
      config.set(distance_units="cm")
      rd = Rd()

      print(rd.get_angle())
      print(rd.get_coordinate())
      print(rd.OutputDump())
      print(rd.get_distance())
      print(rd.Kalman_Test(100,1,5,"Test2","Test2"))
      print(rd.Calibrate_Kalman())
      

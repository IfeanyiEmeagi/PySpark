from pyspark.sql import SparkSession


def main():
    # Define the sparkSession, name the spark app, instruct the spark to run locally and use all the cores available

    spark = (
        SparkSession.builder.appName("FirstSparkApp").master("local[*]").getOrCreate()
    )

    # Create the data
    data = [
        ("Alice", 25),
        ("Bob", 30),
        ("Charlie", 41),
    ]

    # Assign the columns name
    columns = ["Name", "Age"]

    # Create a DataFrame
    df = spark.createDataFrame(data=data, schema=columns)

    # Show the DataFrame Schema
    print("DataFrame Schema:")
    df.printSchema()

    # Show the DataFrame
    print("Actual DataFrame:")
    df.show()

    print("Data processed successfully")

    # Stop the session to free up resources
    spark.stop()

    print("Spark session stopped")


if __name__ == "__main__":
    main()

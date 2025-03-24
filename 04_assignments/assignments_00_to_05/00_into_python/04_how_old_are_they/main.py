def how_old_are_they():
    anton:int = 21
    beth:int = 6 + anton
    chen:int = 20 + beth
    drew:int = chen + anton
    ethan:int = chen

    print(f"Anton is: {str(anton)}")
    print(f"Beth is: {str(beth)}")
    print(f"Chen is: {str(chen)}")
    print(f"Drew is: {str(drew)}")
    print(f"Ethan is: {str(ethan)}")


if __name__ == '__main__':
    how_old_are_they()
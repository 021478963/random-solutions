public class WateringPlants {
  
  public static void main(String[] args) {
    System.out.println(wateringPlants(new int[]{7,7,7,7,7,7,7}, 8));
  }

  public static int wateringPlants(int[] plants, int capacity) {
    int currentPlant = 0;
    int currentWater = capacity;
    int steps = 0;

    do {
      if (currentWater >= plants[currentPlant]) {
        steps++;
        currentWater -= plants[currentPlant];
      } else {
        steps += 2 * currentPlant + 1;
        currentWater = capacity - plants[currentPlant];
      }
      currentPlant++;
    } while (currentPlant != plants.length);
    return steps;
  }
}

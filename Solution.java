import java.util.*;

public class Solution {
    public static int maxMeetings(int[] effectiveness) {
        // Separate the positive and negative values
        List<Integer> positives = new ArrayList<>();
        List<Integer> negatives = new ArrayList<>();
        
        for (int value : effectiveness) {
            if (value > 0) {
                positives.add(value);
            } else if (value < 0) {
                negatives.add(value);
            }
        }
        
        // Sort positive values in descending order and negatives in ascending order
        positives.sort(Collections.reverseOrder());
        negatives.sort(Comparator.naturalOrder());
        
        // Initialize the index and the count of meetings
        int index = 0;
        int meetingCount = 0;
        
        // Add positive effectiveness values first
        for (int value : positives) {
            index += value;
            meetingCount++;
        }
        
        // Try to add negative values
        for (int value : negatives) {
            if (index + value > 0) { // Only add if it keeps the index positive
                index += value;
                meetingCount++;
            } else {
                break; // Stop if adding the next negative value makes the index non-positive
            }
        }
        
        return meetingCount;
    }

    public static void main(String[] args) {
        int[] effectiveness = {-3, 0, 2, 1};
        System.out.println(maxMeetings(effectiveness)); // Output: 3
    }
}
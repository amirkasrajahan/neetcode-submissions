class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] leftArr = new int[nums.length];
        leftArr[0] = 1;
        int[] rightArr = new int[nums.length];
        rightArr[nums.length-1] = 1;

        int[] resultArr = new int[nums.length];

        for(int i = 1; i < nums.length; i++){
            leftArr[i] = leftArr[i-1] * nums[i-1];
        }
        for(int j = nums.length - 2; j >= 0 ; j--){
            rightArr[j] = rightArr[j+1] * nums[j+1];
        }
        for(int i = 0; i < nums.length; i++){
            resultArr[i] = rightArr[i] * leftArr[i];
        }
    return resultArr;
    }
}

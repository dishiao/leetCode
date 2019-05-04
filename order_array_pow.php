class Solution {

    /**
     * @param Integer[] $A
     * @return Integer[]
     */
    function sortedSquares($A) {
        $arr = [];
        foreach($A as $key=>$value){
           $arr[] = pow($value,2);
        }
        asort($arr);
        return $arr;
    }
}

class Solution {

    /**
     * @param String[] $words
     * @return Integer
     */
    function uniqueMorseRepresentations($words) {
        // 输出26个字母
        $arr_key = [];
        for($i=65;$i<91;$i++){
             $arr_key[] = strtolower(chr($i));//输出小写字母
        }
        // 摩尔斯码的数组
        $arr_value = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."];
        // 对应26个字母的摩尔斯码
        $arr = array_combine($arr_key,$arr_value);
        $check_arr_all = [];
        foreach($words as  $value){
            $value = str_split($value);
            $check = '';
            foreach($value as $v){
                $check.=$arr[$v];
            }
            $check_arr_all[] = $check;
        }
        // 去重
        $check_arr_all = array_unique($check_arr_all);
        return count($check_arr_all);
    }
}

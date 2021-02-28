import Data.List

--inp =  [19,20,14,0,9,1]
--
--pGame xs n = pGame' (reverse xs) n
--
--pGame' xs n =  [x | x <- [19,20,14,0,9,1..n]]

--playGame :: [Int] -> Int -> Int
playGame xs n = playGame' n (reverse xs)

playGame' :: Int -> [Int] -> Int
playGame' n (t:ts) 
    | length (t:ts) == n = t
    | otherwise  = playGame' n (whereIs t ts 1 : t : ts)

--    | t `elem` ts = playGame' n (getIndex (elemIndex t ts) : t : ts) 
whereIs n (t:ts) c 
    | n == t = c
    | otherwise = whereIs n ts (c+1)
whereIs n [] c = 
    
getIndex :: Maybe Int -> Int
getIndex (Just x) = x +1
getIndex Nothing = 0
--    (concat [(elemIndex t ts), (t:ts)])
--    | otherwise = playGame' n 0 : t : ts
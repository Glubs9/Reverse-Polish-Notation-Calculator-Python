import Control.Monad

main = forever $ do
        putStrLn "enter: "
        l <- getLine
        print $ rpn' l

rft = tail . tail
n2 = head . tail
n1 = head
app :: (Int -> Int -> Int) -> [Int] -> [Int]
app func li_in = (func (n2 li_in) (n1 li_in)):(rft li_in)

rpn :: [String] -> [Int]
rpn [] = []
rpn li_in
        | l == "+" = app (+) ret
        | l == "-" = app (-) ret
        | l == "*" = app (*) ret
        | l == "/" = app div ret 
        | otherwise = (read l :: Int):ret
        where i = init li_in
              l = last li_in
              ret = rpn (init li_in)

rpn' = (head . rpn . words)

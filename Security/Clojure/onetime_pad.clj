(ns onetime-pad.core)

(defn rand-bytes [size]
  (let [rand (java.security.SecureRandom/getInstance "SHA1PRNG")
        buffer (make-array Byte/TYPE size)]
    (.nextBytes rand buffer) 
    buffer))


(defn encrypt [m]
  (let [message (map int m)
        size (count message)
        key (rand-bytes size)
        enc-message (map bit-xor message key)]
    {:bin-key (vec key) :msg (vec enc-message)}))


(defn decrypt [pad message]
  (apply str 
       (map char
          (map bit-xor message pad))))


(let [x (encrypt "joão canavarro jvcanavarro@gmail.com")] (def enc_message x))
(println (second enc_message))

(let [x (decrypt (:bin-key enc_message) (:msg enc_message))] (def dec_message x))
(println dec_message)

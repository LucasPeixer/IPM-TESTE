import { useNavigate } from "react-router-dom";
import { IoArrowBackSharp } from "react-icons/io5";

const BackButton = ({to}) => {
  const navigate = useNavigate();

  const handleBack = () => {
    if (to) {
      navigate(to);
    } else {
      navigate(-1);
    }
  };

  return (
    <button
      onClick={handleBack}
      className="absolute top-4 left-4 text-gray-600 hover:text-gray-800"
    >
      <IoArrowBackSharp size={24} />
    </button>
  );
};

export default BackButton;

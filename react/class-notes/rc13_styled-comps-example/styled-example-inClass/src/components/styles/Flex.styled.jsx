import styled from "styled-components";

const Flex = styled.div`
  display: flex;
  align-items: center;
  /* justify-content: space-between; */
  gap: 2rem;
  & div,
  & ul {
    /*!Tüm elemanların buyumesine izin ver*/
    flex-grow: 1;
    /* Tüm div'lerin eşit miktarda alan tutabilmesine izin ver.*/
    flex-basis: 0;
  }
  @media (max-width: ${({ theme }) => theme.responsive}) {
    flex-direction: column;
    text-align: center;
  }
`;

export default Flex;
